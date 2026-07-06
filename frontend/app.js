// Testing Environment Frontend JavaScript

function testGreeting() {
    const nameInput = document.getElementById('nameInput');
    const output = document.getElementById('greetingOutput');
    const name = nameInput.value.trim() || 'Guest';

    output.textContent = `✓ Hello, ${name}! Frontend is working correctly.`;
    output.style.color = '#28a745';
}

async function testAPI() {
    const output = document.getElementById('apiOutput');
    output.textContent = 'Testing API connection...';
    output.style.color = '#666';

    try {
        // Simulating API call for testing purposes
        await new Promise(resolve => setTimeout(resolve, 1000));

        const testData = {
            status: 'success',
            timestamp: new Date().toISOString(),
            message: 'API endpoint is reachable',
            response_time: '120ms'
        };

        output.innerHTML = `
            ✓ API Test Result:<br>
            Status: ${testData.status}<br>
            Timestamp: ${testData.timestamp}<br>
            Message: ${testData.message}<br>
            Response Time: ${testData.response_time}
        `;
        output.style.color = '#28a745';
    } catch (error) {
        output.textContent = `✗ API Error: ${error.message}`;
        output.style.color = '#dc3545';
    }
}

function loadTestData() {
    const output = document.getElementById('dataOutput');

    const testUsers = [
        { id: 1, name: 'Alice Johnson', role: 'Developer', status: 'Active' },
        { id: 2, name: 'Bob Smith', role: 'Tester', status: 'Active' },
        { id: 3, name: 'Charlie Brown', role: 'Designer', status: 'Active' }
    ];

    let tableHTML = `
        <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
            <thead>
                <tr style="background: #667eea; color: white;">
                    <th style="padding: 10px; text-align: left;">ID</th>
                    <th style="padding: 10px; text-align: left;">Name</th>
                    <th style="padding: 10px; text-align: left;">Role</th>
                    <th style="padding: 10px; text-align: left;">Status</th>
                </tr>
            </thead>
            <tbody>
    `;

    testUsers.forEach(user => {
        tableHTML += `
            <tr style="border-bottom: 1px solid #ddd;">
                <td style="padding: 10px;">${user.id}</td>
                <td style="padding: 10px;">${user.name}</td>
                <td style="padding: 10px;">${user.role}</td>
                <td style="padding: 10px;">
                    <span style="background: #d4edda; color: #155724; padding: 4px 12px; border-radius: 12px; font-size: 12px;">
                        ${user.status}
                    </span>
                </td>
            </tr>
        `;
    });

    tableHTML += `
            </tbody>
        </table>
        <p style="margin-top: 15px; color: #28a745;">✓ Successfully loaded ${testUsers.length} records</p>
    `;

    output.innerHTML = tableHTML;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('✓ Frontend application initialized successfully');
    console.log('✓ All JavaScript functions loaded');
});
