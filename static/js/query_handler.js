document.addEventListener("DOMContentLoaded", () => {
    const queryResultDiv = document.getElementById("query-result");

    document.getElementById("execute-query").addEventListener("click", async () => {
        const queryInput = document.getElementById("query-input").value.trim();

        if (!queryInput) {
            alert("Please enter a query.");
            return;
        }

        try {
            const response = await fetch("/execute_query", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: queryInput }),
            });

            if (!response.ok) throw new Error("Failed to execute query");

            const data = await response.json();

            // Clear previous results
            queryResultDiv.innerHTML = ""; // Ensure queryResultDiv exists.

            // Create Table
            const table = document.createElement("table");
            table.className = "table-auto w-full border-collapse border border-gray-300";

            // Add Header
            const thead = document.createElement("thead");
            thead.id = "resultsTableHeader"; // Create dynamically if needed.

            const headerRow = document.createElement("tr");
            data.columns.forEach((column) => {
                const th = document.createElement("th");
                th.textContent = column;
                th.className = "px-4 py-2 border border-gray-300 bg-gray-200";
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);

            // Add Body
            const tbody = document.createElement("tbody");
            data.rows.forEach((row) => {
                const tr = document.createElement("tr");
                row.forEach((cell) => {
                    const td = document.createElement("td");
                    td.textContent = cell;
                    td.className = "px-4 py-2 border border-gray-300";
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);

            queryResultDiv.appendChild(table);
        } catch (error) {
            console.error("Error executing query:", error);
            alert("Failed to execute query.");
        }
    });
});
