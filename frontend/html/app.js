const API_BASE = 'http://localhost:5000';

const tbody     = document.getElementById('team-tbody');
const badge     = document.getElementById('status-badge');
const statusTxt = document.getElementById('status-text');
const errorMsg  = document.getElementById('error-msg');

function setBadge(online) {
  badge.className    = 'online' + (!online ? ' offline' : '');
  statusTxt.textContent = online ? 'backend online' : 'backend offline';
  if (!online) badge.classList.replace('online', 'offline');
}

function estadoPill(estado) {
  const map = {
    ok:      { cls: 'pill-ok',    label: 'OK'      },
    warn:    { cls: 'pill-warn',  label: 'WARN'    },
    error:   { cls: 'pill-error', label: 'ERROR'   },
  };
  const e   = (estado || '').toLowerCase();
  const cfg = map[e] || { cls: 'pill-warn', label: estado || '?' };
  return `<span class="pill ${cfg.cls}">${cfg.label}</span>`;
}

function renderTable(members) {
  if (!members || members.length === 0) {
    tbody.innerHTML = '<tr><td colspan="5" id="loading">Sin datos.</td></tr>';
    return;
  }

  tbody.innerHTML = members.map(m => `
    <tr>
      <td class="td-name">${m.nombre} ${m.apellido}</td>
      <td class="td-legajo">${m.legajo}</td>
      <td class="td-feature">${m.feature}</td>
      <td class="td-service">${m.servicio}</td>
      <td>${estadoPill(m.estado)}</td>
    </tr>
  `).join('');
}

async function loadTeam() {
  try {
    const res = await fetch(`${API_BASE}/api/team`);

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const data = await res.json();
    setBadge(true);
    renderTable(data);

  } catch (err) {
    console.error('Error al cargar equipo:', err);
    setBadge(false);
    tbody.innerHTML = '';
    errorMsg.style.display = 'block';
  }
}

loadTeam();