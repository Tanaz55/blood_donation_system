document.addEventListener("DOMContentLoaded", () => {
            console.log("Document ready");

            document.body.addEventListener("click", async (event) => {
                if (event.target.classList.contains("table-btn")) {
                    const tableName = event.target.id;
                    console.log("Fetching columns for:", tableName);

                    try {
                        const response = await fetch(`/get_columns/${tableName}`);
                        if (!response.ok) {
                            throw new Error("Failed to fetch column names");
                        }
                        const columnNames = await response.json();

                        const columnsBox = document.getElementById("columns");
                        columnsBox.value = columnNames.join(", ");
                    } catch (error) {
                        console.error("Error fetching columns:", error);
                        alert("Failed to fetch column names. Please try again.");
                    }
                }
            });
        });