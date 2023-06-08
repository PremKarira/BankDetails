// Disable input fields
const formInputs = document.querySelectorAll('#bank-details-container input');
formInputs.forEach(input => {
  input.disabled = true;
});
function fill(email){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const bankdetailsParam = urlParams.get('bankdetails');
    const bankDetails = JSON.parse(decodeURIComponent(bankdetailsParam));
    
    document.getElementById('email').textContent = bankDetails.email;
    document.getElementById('account-holder-name').textContent = bankDetails.account_holder_name;
    document.getElementById('account-number').textContent = bankDetails.account_number;
    document.getElementById('ifsc-code').textContent = bankDetails.ifsc_code;
    document.getElementById('bank-name').textContent = bankDetails.bank_name;
    document.getElementById('branch-name').textContent = bankDetails.branch_name;
    
}