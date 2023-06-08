document.addEventListener('DOMContentLoaded', () => {
  getUsers();
  getBankDetails();
  getUpdateRequests();
});

function getUsers() {
  // Fetch the list of users from the backend API
  fetch('http://localhost:8080/api/users')
    .then(response => response.json())
    .then(data => {
      const userList = document.getElementById('user-list-items');
      userList.innerHTML = '';
      data.forEach(user => {
        const listItem = document.createElement('li');
        listItem.textContent = `${user.email} - ${user.password}`;
        userList.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function getBankDetails() {
  // Fetch the bank details from the backend API
  fetch('http://localhost:8080/api/bankdetails')
    .then(response => response.json())
    .then(data => {
      const bankDetailsBody = document.getElementById('bank-details-body');
      bankDetailsBody.innerHTML = '';
      data.forEach(details => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${details.email}</td>
          <td>${details.account_holder_name}</td>
          <td>${details.account_number}</td>
          <td>${details.ifsc_code}</td>
          <td>${details.bank_name}</td>
          <td>${details.branch_name}</td>
        `;
        bankDetailsBody.appendChild(row);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
function getUpdateRequests() {
  // Fetch the update requests from the backend API
  fetch('http://localhost:8080/api/bankdetails/updates')
    .then(response => response.json())
    .then(data => {
      const updateRequestsList = document.getElementById('update-request-body');
      updateRequestsList.innerHTML = '';
      data.forEach(request => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${request.email}</td>
          <td>${request.account_holder_name}</td>
          <td>${request.account_number}</td>
          <td>${request.ifsc_code}</td>
          <td>${request.bank_name}</td>
          <td>${request.branch_name}</td>
          <td><button class="update-request-button" data-request='${JSON.stringify(request)}'>Send Update Request</button></td>
        `;
        updateRequestsList.appendChild(row);
      });

      // Add event listeners to the buttons
      const buttons = document.getElementsByClassName('update-request-button');
      Array.from(buttons).forEach(button => {
        button.addEventListener('click', sendUpdateRequest);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function sendUpdateRequest(event) {
  const requestData = JSON.parse(event.target.getAttribute('data-request'));

  fetch('http://localhost:8080/api/bankdetails/updates', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestData),
  })
    .then(response => response.json())
    .then(data => {
      // Handle the response if needed
      // console.log(data);
      location.reload();
    })
    .catch(error => {
      console.error('Error:', error);
    });
}