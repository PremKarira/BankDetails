function add() {
  const form = document.getElementById('add-new');
  const email = form.elements.email.value;
  const accountHolderName = form.elements.account_holder_name.value;
  const accountNumber = form.elements.account_number.value;
  const ifscCode = form.elements.ifsc_code.value;
  const bankName = form.elements.bank_name.value;
  const branchName = form.elements.branch_name.value;


  const payload = {
    email: email,
    account_holder_name: accountHolderName,
    account_number: accountNumber,
    ifsc_code: ifscCode,
    bank_name: bankName,
    branch_name: branchName
  };

  fetch('http://localhost:8080/api/bankdetails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload)
  })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to add book');
      }
    })
    .then(data => {
      const confirmationMessage = document.getElementById('confirmation-message');
      confirmationMessage.textContent = 'Details added successfully!';
      confirmationMessage.style.display = 'block';
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
function update() {
  const form = document.getElementById('update');
  const email = form.elements.email.value;
  const accountHolderName = form.elements.account_holder_name.value;
  const accountNumber = form.elements.account_number.value;
  const ifscCode = form.elements.ifsc_code.value;
  const bankName = form.elements.bank_name.value;
  const branchName = form.elements.branch_name.value;


  const payload = {
    email: email,
    account_holder_name: accountHolderName,
    account_number: accountNumber,
    ifsc_code: ifscCode,
    bank_name: bankName,
    branch_name: branchName
  };

  fetch(`http://localhost:8080/api/bankdetails/${urlParams.get('id')}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload)
  })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to add book');
      }
    })
    .then(data => {
      const confirmationMessage = document.getElementById('confirmation-message');
      confirmationMessage.textContent = 'Details sent for update after acceptance!';
      confirmationMessage.style.display = 'block';
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
