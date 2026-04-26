let state = null;

async function init() {
    let rows = document.getElementById("rows").value;
    let cols = document.getElementById("cols").value;

    let res = await fetch('http://127.0.0.1:5000/init', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({rows, cols})
    });

    state = await res.json();
    render();
}

async function step() {
    let res = await fetch('http://127.0.0.1:5000/step');
    state = await res.json();
    render();
}

function render() {
    let gridDiv = document.getElementById("grid");
    gridDiv.innerHTML = "";

    let grid = state.grid;

    for (let i = 0; i < grid.length; i++) {
        let row = document.createElement("div");

        for (let j = 0; j < grid[0].length; j++) {
            let cell = document.createElement("span");
            cell.className = "cell";

            let isVisited = state.visited.some(v => v[0]==i && v[1]==j);
            let isSafe = state.safe.some(s => s[0]==i && s[1]==j);

            if (state.position[0]==i && state.position[1]==j) {
                cell.style.background = "blue";
            } else if (isSafe) {
                cell.style.background = "green";
            } else if (isVisited) {
                cell.style.background = "lightgray";
            } else {
                cell.style.background = "gray";
            }

            if (grid[i][j] === 'P' || grid[i][j] === 'W') {
                cell.style.background = "red";
            }

            row.appendChild(cell);
        }

        gridDiv.appendChild(row);
    }

    document.getElementById("metrics").innerText =
        "Steps: " + state.steps + " | Percepts: " + state.percepts.join(", ");
}