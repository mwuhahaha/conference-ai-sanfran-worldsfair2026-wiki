import Graph from "https://esm.sh/graphology@0.26.0";
import Sigma from "https://esm.sh/sigma@3.0.3";

const TEMPLATE_ROLES = {
  vendor_concept: new Set(["vendor", "concept"]),
  person_concept: new Set(["person", "concept"]),
  concept_concept: new Set(["concept"]),
};
const ROLE_COLORS = {
  vendor: "#0f766e",
  person: "#b45309",
  concept: "#2563eb",
  evidence: "#64748b",
  organization: "#475569",
};
const TEMPLATE_LABELS = {
  vendor_concept: "Vendors + Concepts",
  person_concept: "People + Concepts",
  concept_concept: "Concepts + Concepts",
};

const root = document.querySelector("#relationship-explorer");
const status = document.querySelector("#relationship-status");
const search = document.querySelector("#relationship-search");
const searchResults = document.querySelector("#relationship-search-results");
const compareLabel = document.querySelector("#relationship-compare-label");
const compare = document.querySelector("#relationship-compare");
const compareResults = document.querySelector("#relationship-compare-results");
const layer = document.querySelector("#relationship-layer");
const relationType = document.querySelector("#relationship-type");
const includeDerived = document.querySelector("#relationship-derived");
const canvas = document.querySelector("#relationship-canvas");
const emptyGraph = document.querySelector("#relationship-graph-empty");
const landscape = document.querySelector("#relationship-landscape");
const list = document.querySelector("#relationship-list");
const matrix = document.querySelector("#relationship-matrix");
const detail = document.querySelector("#relationship-detail");
const expand = document.querySelector("#relationship-expand");
const tabs = [...document.querySelectorAll("[data-relationship-view]")];
const templates = [...document.querySelectorAll("[data-relationship-template]")];

const data = await fetch("/relationship-data.json").then((response) => {
  if (!response.ok) throw new Error(`Relationship request failed: ${response.status}`);
  return response.json();
});

const nodes = new Map((data.nodes || []).map((node) => [node.id, node]));
const relationships = data.relationships || [];
const roleIds = new Map();
Object.entries(data.roles || {}).forEach(([plural, ids]) => {
  const role = plural === "vendors" ? "vendor" : plural === "people" ? "person" : plural === "concepts" ? "concept" : plural;
  ids.forEach((id) => roleIds.set(id, role));
});
for (const node of nodes.values()) {
  if (!roleIds.has(node.id)) roleIds.set(node.id, node.role || "evidence");
}

const params = new URLSearchParams(location.search);
let activeTemplate = TEMPLATE_ROLES[params.get("template")] ? params.get("template") : "vendor_concept";
let activeView = ["landscape", "graph", "list", "matrix"].includes(params.get("view")) ? params.get("view") : "landscape";
let selectedId = nodes.has(params.get("entity")) ? params.get("entity") : "";
let compareId = nodes.has(params.get("compare")) ? params.get("compare") : "";
if (activeTemplate !== "concept_concept" || nodeRole(compareId) !== "concept") compareId = "";
let selectedRelationshipId = "";
let renderer = null;
let focusedGraph = null;
let expanded = false;

function nodeRole(id) {
  return roleIds.get(id) || "evidence";
}

function nodeTitle(id) {
  return nodes.get(id)?.title || id;
}

function templateRelationships() {
  return relationships.filter((relationship) => relationship.template === activeTemplate);
}

function filteredRelationships({incident = true} = {}) {
  return templateRelationships().filter((relationship) => {
    if (!includeDerived.checked && relationship.derivation !== "explicit") return false;
    if (layer.value && !(relationship.sourceLayers || []).includes(layer.value)) return false;
    if (relationType.value && relationship.relationType !== relationType.value) return false;
    if (incident && selectedId && relationship.source !== selectedId && relationship.target !== selectedId) return false;
    if (incident && compareId && !(
      (relationship.source === selectedId && relationship.target === compareId) ||
      (relationship.source === compareId && relationship.target === selectedId)
    )) return false;
    return true;
  });
}

function eligibleSearchNodes() {
  const roles = TEMPLATE_ROLES[activeTemplate];
  const ids = new Set();
  templateRelationships().forEach((relationship) => {
    ids.add(relationship.source);
    ids.add(relationship.target);
  });
  return [...ids]
    .map((id) => nodes.get(id))
    .filter((node) => node && roles.has(nodeRole(node.id)))
    .sort((left, right) => left.title.localeCompare(right.title));
}

function syncUrl() {
  const next = new URL(location.href);
  next.searchParams.set("template", activeTemplate);
  next.searchParams.set("view", activeView);
  selectedId ? next.searchParams.set("entity", selectedId) : next.searchParams.delete("entity");
  activeTemplate === "concept_concept" && compareId ? next.searchParams.set("compare", compareId) : next.searchParams.delete("compare");
  includeDerived.checked ? next.searchParams.delete("derivation") : next.searchParams.set("derivation", "explicit");
  layer.value ? next.searchParams.set("layer", layer.value) : next.searchParams.delete("layer");
  relationType.value ? next.searchParams.set("relation", relationType.value) : next.searchParams.delete("relation");
  history.replaceState({}, "", next);
}

function setTemplate(template) {
  activeTemplate = template;
  selectedId = "";
  compareId = "";
  selectedRelationshipId = "";
  search.value = "";
  compare.value = "";
  detail.classList.remove("open");
  expanded = false;
  update();
}

function setView(view) {
  activeView = view;
  update();
}

function selectNode(id, preferredView = "graph") {
  if (!nodes.has(id)) return;
  selectedId = id;
  search.value = nodeTitle(id);
  if (preferredView) activeView = preferredView;
  selectedRelationshipId = "";
  detail.classList.remove("open");
  expanded = false;
  update();
}

function selectCompareNode(id) {
  if (!nodes.has(id) || nodeRole(id) !== "concept" || id === selectedId) return;
  compareId = id;
  compare.value = nodeTitle(id);
  activeView = "graph";
  selectedRelationshipId = "";
  detail.classList.remove("open");
  update();
}

function relationLabel(value) {
  return String(value || "related to").replaceAll("_", " ");
}

function evidenceLabel(value) {
  return String(value || "source").replaceAll("_", " ");
}

function clearElement(element) {
  element.replaceChildren();
}

function button(text, className, onClick) {
  const item = document.createElement("button");
  item.type = "button";
  item.className = className;
  item.textContent = text;
  item.addEventListener("click", onClick);
  return item;
}

function linkForNode(id) {
  const node = nodes.get(id);
  const link = document.createElement("a");
  link.href = node?.url || `/${id}/`;
  link.textContent = node?.title || id;
  return link;
}

function renderLandscape() {
  clearElement(landscape);
  const conceptIds = data.roles?.concepts || [];
  const table = document.createElement("table");
  table.className = "relationship-table";
  table.innerHTML = "<thead><tr><th>Concept</th><th>Vendors</th><th>People</th><th>Connected concepts</th><th>Evidence</th></tr></thead>";
  const body = document.createElement("tbody");
  conceptIds
    .map((id) => nodes.get(id))
    .filter(Boolean)
    .sort((left, right) => left.title.localeCompare(right.title))
    .forEach((concept) => {
      const related = relationships.filter((relationship) => relationship.source === concept.id || relationship.target === concept.id);
      const opposite = (relationship) => relationship.source === concept.id ? relationship.target : relationship.source;
      const countRole = (role) => new Set(related.map(opposite).filter((id) => nodeRole(id) === role)).size;
      const evidenceCount = new Set(related.flatMap((relationship) => (relationship.evidence || []).map((item) => item.id))).size;
      const row = document.createElement("tr");
      const title = document.createElement("td");
      title.append(button(concept.title, "relationship-text-button", () => selectNode(concept.id)));
      [title, countRole("vendor"), countRole("person"), countRole("concept"), evidenceCount].forEach((value) => {
        const cell = value instanceof HTMLElement ? value : document.createElement("td");
        if (!(value instanceof HTMLElement)) cell.textContent = value.toLocaleString();
        row.append(cell);
      });
      body.append(row);
    });
  table.append(body);
  const wrap = document.createElement("div");
  wrap.className = "relationship-table-wrap";
  wrap.append(table);
  landscape.append(wrap);
}

function renderList() {
  clearElement(list);
  const rows = filteredRelationships();
  const table = document.createElement("table");
  table.className = "relationship-table";
  table.innerHTML = "<thead><tr><th>Source</th><th>Relationship</th><th>Target</th><th>Basis</th><th>Evidence</th></tr></thead>";
  const body = document.createElement("tbody");
  rows
    .slice()
    .sort((left, right) => nodeTitle(left.source).localeCompare(nodeTitle(right.source)) || nodeTitle(left.target).localeCompare(nodeTitle(right.target)))
    .forEach((relationship) => {
      const row = document.createElement("tr");
      row.tabIndex = 0;
      row.addEventListener("click", () => showRelationship(relationship.id));
      row.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          showRelationship(relationship.id);
        }
      });
      const source = document.createElement("td");
      source.append(linkForNode(relationship.source));
      const relation = document.createElement("td");
      relation.textContent = relationLabel(relationship.relationType);
      const target = document.createElement("td");
      target.append(linkForNode(relationship.target));
      const basis = document.createElement("td");
      basis.textContent = relationship.derivation === "explicit" ? "Direct" : "Labeled derived";
      const evidence = document.createElement("td");
      evidence.textContent = (relationship.evidence || []).length.toLocaleString();
      row.append(source, relation, target, basis, evidence);
      body.append(row);
    });
  table.append(body);
  const wrap = document.createElement("div");
  wrap.className = "relationship-table-wrap";
  wrap.append(table);
  list.append(wrap);
  if (!rows.length) list.append(emptyMessage("No relationships match the current filters."));
}

function emptyMessage(text) {
  const message = document.createElement("p");
  message.className = "relationship-empty";
  message.textContent = text;
  return message;
}

function roleAxis() {
  if (activeTemplate === "vendor_concept") return ["vendor", "concept"];
  if (activeTemplate === "person_concept") return ["person", "concept"];
  return ["concept", "concept"];
}

function renderMatrix() {
  clearElement(matrix);
  const rows = filteredRelationships();
  const [rowRole, columnRole] = roleAxis();
  const rowIds = new Set();
  const columnIds = new Set();
  const counts = new Map();
  for (const relationship of rows) {
    const sourceRole = nodeRole(relationship.source);
    const targetRole = nodeRole(relationship.target);
    let rowId = sourceRole === rowRole ? relationship.source : relationship.target;
    let columnId = targetRole === columnRole ? relationship.target : relationship.source;
    if (activeTemplate === "concept_concept") {
      [rowId, columnId] = [relationship.source, relationship.target].sort((left, right) => nodeTitle(left).localeCompare(nodeTitle(right)));
    }
    if (nodeRole(rowId) !== rowRole || nodeRole(columnId) !== columnRole) continue;
    rowIds.add(rowId);
    columnIds.add(columnId);
    counts.set(`${rowId}\u0000${columnId}`, (counts.get(`${rowId}\u0000${columnId}`) || 0) + 1);
    if (activeTemplate === "concept_concept") {
      counts.set(`${columnId}\u0000${rowId}`, (counts.get(`${columnId}\u0000${rowId}`) || 0) + 1);
      rowIds.add(columnId);
      columnIds.add(rowId);
    }
  }
  let rowNodes = [...rowIds].sort((left, right) => nodeTitle(left).localeCompare(nodeTitle(right)));
  let columnNodes = [...columnIds].sort((left, right) => nodeTitle(left).localeCompare(nodeTitle(right)));
  if (selectedId) {
    if (rowIds.has(selectedId)) rowNodes = [selectedId];
    if (activeTemplate !== "concept_concept" && columnIds.has(selectedId)) columnNodes = [selectedId];
  }
  const table = document.createElement("table");
  table.className = "relationship-table relationship-matrix";
  const head = document.createElement("thead");
  const header = document.createElement("tr");
  const corner = document.createElement("th");
  corner.textContent = `${rowRole} / ${columnRole}`;
  header.append(corner);
  columnNodes.forEach((id) => {
    const cell = document.createElement("th");
    cell.textContent = nodeTitle(id);
    cell.title = nodeTitle(id);
    header.append(cell);
  });
  head.append(header);
  const body = document.createElement("tbody");
  rowNodes.forEach((rowId) => {
    const row = document.createElement("tr");
    const label = document.createElement("th");
    label.append(button(nodeTitle(rowId), "relationship-text-button", () => selectNode(rowId, "matrix")));
    row.append(label);
    columnNodes.forEach((columnId) => {
      const cell = document.createElement("td");
      const count = counts.get(`${rowId}\u0000${columnId}`) || 0;
      if (count) {
        cell.append(button(count.toLocaleString(), "relationship-matrix-cell", () => {
          const match = rows.find((relationship) => new Set([relationship.source, relationship.target]).has(rowId) && new Set([relationship.source, relationship.target]).has(columnId));
          if (match) showRelationship(match.id);
        }));
      }
      row.append(cell);
    });
    body.append(row);
  });
  table.append(head, body);
  const wrap = document.createElement("div");
  wrap.className = "relationship-table-wrap relationship-matrix-wrap";
  wrap.append(table);
  matrix.append(wrap);
  if (!rows.length) matrix.append(emptyMessage("No matrix cells match the current filters."));
}

function graphPosition(id, role, index, total) {
  const hash = [...id].reduce((value, character) => Math.imul(value ^ character.charCodeAt(0), 16777619), 2166136261) >>> 0;
  const jitter = ((hash % 1000) / 1000 - 0.5) * 0.28;
  if (activeTemplate === "concept_concept") {
    const angle = (index / Math.max(total, 1)) * Math.PI * 2;
    return {x: Math.cos(angle), y: Math.sin(angle)};
  }
  const x = role === "concept" ? 0.9 : -0.9;
  const y = total <= 1 ? 0 : -0.9 + (index / (total - 1)) * 1.8;
  return {x: x + jitter, y};
}

function renderGraph() {
  expand.hidden = true;
  if (renderer) {
    renderer.kill();
    renderer = null;
  }
  clearElement(canvas);
  const eligible = selectedId ? filteredRelationships() : [];
  const limitedRelationships = [];
  const visibleIds = new Set(selectedId ? [selectedId] : []);
  for (const relationship of eligible) {
    if (limitedRelationships.length >= (expanded ? 80 : 60)) break;
    const additions = [relationship.source, relationship.target].filter((id) => !visibleIds.has(id));
    if (visibleIds.size + additions.length > (expanded ? 40 : 26)) continue;
    additions.forEach((id) => visibleIds.add(id));
    limitedRelationships.push(relationship);
  }
  emptyGraph.hidden = Boolean(selectedId && limitedRelationships.length);
  if (!selectedId) {
    emptyGraph.textContent = "Choose a vendor, person, or concept to draw a focused relationship scene.";
    return;
  }
  if (!limitedRelationships.length) {
    emptyGraph.textContent = "No focused relationships match the current filters.";
    return;
  }
  const graph = new Graph({type: "undirected", multi: true});
  const idsByRole = new Map();
  visibleIds.forEach((id) => {
    const role = nodeRole(id);
    if (!idsByRole.has(role)) idsByRole.set(role, []);
    idsByRole.get(role).push(id);
  });
  idsByRole.forEach((ids, role) => ids.sort((left, right) => nodeTitle(left).localeCompare(nodeTitle(right))).forEach((id, index) => {
    const point = graphPosition(id, role, index, ids.length);
    graph.addNode(id, {
      x: point.x,
      y: point.y,
      label: nodeTitle(id),
      role,
      color: ROLE_COLORS[role] || ROLE_COLORS.evidence,
      size: id === selectedId ? 12 : 8,
      forceLabel: true,
    });
  }));
  limitedRelationships.forEach((relationship, index) => {
    graph.addEdgeWithKey(`relationship-${index}`, relationship.source, relationship.target, {
      relationshipId: relationship.id,
      color: relationship.derivation === "explicit" ? "#475569" : "#b7791f",
      size: relationship.derivation === "explicit" ? 1.4 : 1,
    });
  });
  focusedGraph = graph;
  renderer = new Sigma(graph, canvas, {
    labelDensity: 1,
    labelGridCellSize: 90,
    labelRenderedSizeThreshold: 0,
    zIndex: true,
    renderEdgeLabels: false,
    nodeReducer(node, attributes) {
      return {...attributes, zIndex: node === selectedId ? 2 : 1};
    },
    edgeReducer(edge, attributes) {
      return {...attributes, zIndex: attributes.relationshipId === selectedRelationshipId ? 2 : 1, size: attributes.relationshipId === selectedRelationshipId ? 2.5 : attributes.size};
    },
  });
  renderer.on("clickNode", ({node}) => selectNode(node));
  renderer.on("clickEdge", ({edge}) => showRelationship(graph.getEdgeAttribute(edge, "relationshipId")));
  document.querySelector("#relationship-zoom-in").onclick = () => renderer?.getCamera().animatedZoom({duration: 200});
  document.querySelector("#relationship-zoom-out").onclick = () => renderer?.getCamera().animatedUnzoom({duration: 200});
  document.querySelector("#relationship-fit").onclick = () => renderer?.getCamera().animatedReset({duration: 250});
  const omitted = eligible.length - limitedRelationships.length;
  expand.hidden = omitted <= 0 || expanded;
  emptyGraph.hidden = true;
  if (omitted > 0) status.textContent += ` ${omitted.toLocaleString()} additional relationships are available in List view.`;
}

function showRelationship(id) {
  const relationship = relationships.find((item) => item.id === id);
  if (!relationship) return;
  selectedRelationshipId = id;
  detail.replaceChildren();
  const close = button("×", "relationship-detail-close", () => {
    selectedRelationshipId = "";
    detail.classList.remove("open");
    renderer?.refresh();
  });
  close.setAttribute("aria-label", "Close relationship details");
  const eyebrow = document.createElement("p");
  eyebrow.className = "eyebrow";
  eyebrow.textContent = relationship.derivation === "explicit" ? "Explicit relationship" : "Labeled derived relationship";
  const heading = document.createElement("h2");
  heading.textContent = `${nodeTitle(relationship.source)} ${relationLabel(relationship.relationType)} ${nodeTitle(relationship.target)}`;
  const reason = document.createElement("p");
  reason.textContent = relationship.publicReason || "No public explanation is available.";
  const boundary = document.createElement("p");
  boundary.className = "relationship-boundary";
  boundary.textContent = relationship.boundary || "Use the linked evidence to evaluate this relationship.";
  const layers = document.createElement("p");
  layers.className = "relationship-layer-list";
  layers.textContent = (relationship.sourceLayers || []).map(evidenceLabel).join(" · ");
  const evidenceHeading = document.createElement("h3");
  evidenceHeading.textContent = "Evidence path";
  const evidenceList = document.createElement("ol");
  evidenceList.className = "relationship-evidence-list";
  (relationship.evidence || []).forEach((item) => {
    const entry = document.createElement("li");
    entry.append(linkForNode(item.id));
    const meta = document.createElement("small");
    meta.textContent = evidenceLabel(item.sourceLayer);
    entry.append(meta);
    evidenceList.append(entry);
  });
  detail.append(close, eyebrow, heading, reason, layers, boundary, evidenceHeading, evidenceList);
  detail.classList.add("open");
  renderer?.refresh();
}

function populateLayerFilter() {
  const layers = [...new Set(relationships.flatMap((relationship) => relationship.sourceLayers || []))].sort();
  layers.forEach((name) => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = evidenceLabel(name);
    layer.append(option);
  });
  if (layers.includes(params.get("layer"))) layer.value = params.get("layer");
  includeDerived.checked = params.get("derivation") !== "explicit";
}

function populateRelationFilter() {
  const selected = relationType.value || params.get("relation") || "";
  const names = [...new Set(templateRelationships().map((relationship) => relationship.relationType))].sort();
  relationType.replaceChildren();
  const all = document.createElement("option");
  all.value = "";
  all.textContent = "All relationship types";
  relationType.append(all);
  names.forEach((name) => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = relationLabel(name);
    relationType.append(option);
  });
  relationType.value = names.includes(selected) ? selected : "";
}

function renderSearchResults() {
  const query = search.value.trim().toLowerCase();
  if (!query || (selectedId && query === nodeTitle(selectedId).toLowerCase())) {
    searchResults.replaceChildren();
    searchResults.classList.remove("open");
    return;
  }
  const matches = eligibleSearchNodes().filter((node) => `${node.title} ${node.excerpt || ""}`.toLowerCase().includes(query)).slice(0, 10);
  searchResults.replaceChildren(...matches.map((node) => button(`${node.title} · ${nodeRole(node.id)}`, "", () => {
    searchResults.replaceChildren();
    searchResults.classList.remove("open");
    selectNode(node.id);
  })));
  searchResults.classList.toggle("open", Boolean(matches.length));
}

function renderCompareResults() {
  const query = compare.value.trim().toLowerCase();
  if (!query || (compareId && query === nodeTitle(compareId).toLowerCase())) {
    compareResults.replaceChildren();
    compareResults.classList.remove("open");
    return;
  }
  const matches = eligibleSearchNodes()
    .filter((node) => nodeRole(node.id) === "concept" && node.id !== selectedId)
    .filter((node) => `${node.title} ${node.excerpt || ""}`.toLowerCase().includes(query))
    .slice(0, 10);
  compareResults.replaceChildren(...matches.map((node) => button(node.title, "", () => {
    compareResults.replaceChildren();
    compareResults.classList.remove("open");
    selectCompareNode(node.id);
  })));
  compareResults.classList.toggle("open", Boolean(matches.length));
}

function updateControls() {
  templates.forEach((item) => {
    const active = item.dataset.relationshipTemplate === activeTemplate;
    item.classList.toggle("active", active);
    item.setAttribute("aria-pressed", String(active));
  });
  tabs.forEach((item) => {
    const active = item.dataset.relationshipView === activeView;
    item.classList.toggle("active", active);
    item.setAttribute("aria-selected", String(active));
  });
  const placeholderRole = activeTemplate === "vendor_concept" ? "vendor or concept" : activeTemplate === "person_concept" ? "person or concept" : "concept";
  search.placeholder = `Find a ${placeholderRole}`;
  compareLabel.hidden = activeTemplate !== "concept_concept";
}

function updatePanels() {
  if (activeView !== "graph" && renderer) {
    renderer.kill();
    renderer = null;
    focusedGraph = null;
  }
  landscape.hidden = activeView !== "landscape";
  document.querySelector("#relationship-graph-panel").hidden = activeView !== "graph";
  list.hidden = activeView !== "list";
  matrix.hidden = activeView !== "matrix";
}

function updateStatus() {
  const total = templateRelationships().length;
  const filtered = filteredRelationships().length;
  const scope = selectedId ? nodeTitle(selectedId) : TEMPLATE_LABELS[activeTemplate];
  const comparison = compareId ? ` compared with ${nodeTitle(compareId)}` : "";
  status.textContent = `${scope}${comparison}: ${filtered.toLocaleString()} visible relationships from ${total.toLocaleString()} available in this template.`;
}

function update() {
  populateRelationFilter();
  updateControls();
  updatePanels();
  renderLandscape();
  renderList();
  renderMatrix();
  updateStatus();
  if (activeView === "graph") renderGraph();
  syncUrl();
}

templates.forEach((item) => item.addEventListener("click", () => setTemplate(item.dataset.relationshipTemplate)));
tabs.forEach((item) => item.addEventListener("click", () => setView(item.dataset.relationshipView)));
search.addEventListener("input", () => {
  if (selectedId && search.value.trim() !== nodeTitle(selectedId)) selectedId = "";
  renderSearchResults();
});
search.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    const match = eligibleSearchNodes().find((node) => node.title.toLowerCase() === search.value.trim().toLowerCase()) || eligibleSearchNodes().find((node) => node.title.toLowerCase().includes(search.value.trim().toLowerCase()));
    if (match) {
      event.preventDefault();
      selectNode(match.id);
    }
  }
});
compare.addEventListener("input", () => {
  if (compareId && compare.value.trim() !== nodeTitle(compareId)) compareId = "";
  renderCompareResults();
});
compare.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    const query = compare.value.trim().toLowerCase();
    const match = eligibleSearchNodes().find((node) => nodeRole(node.id) === "concept" && node.id !== selectedId && node.title.toLowerCase().includes(query));
    if (match) {
      event.preventDefault();
      selectCompareNode(match.id);
    }
  }
});
layer.addEventListener("change", update);
relationType.addEventListener("change", update);
includeDerived.addEventListener("change", update);
expand.addEventListener("click", () => {
  expanded = true;
  renderGraph();
});

document.querySelector("#relationship-clear").addEventListener("click", () => {
  selectedId = "";
  compareId = "";
  selectedRelationshipId = "";
  search.value = "";
  compare.value = "";
  activeView = "landscape";
  relationType.value = "";
  expanded = false;
  detail.classList.remove("open");
  update();
});

document.querySelector("#relationship-advanced").href = params.get("category")
  ? `/graph/all/?category=${encodeURIComponent(params.get("category"))}`
  : "/graph/all/";

populateLayerFilter();
if (selectedId) search.value = nodeTitle(selectedId);
if (compareId) compare.value = nodeTitle(compareId);
root.dataset.ready = "true";
update();
