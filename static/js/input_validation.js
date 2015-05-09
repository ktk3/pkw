function isValidDate(form)
{
    var dateString = form.input_date.value;
    // First check for the pattern
    var isValid = /^\d{4}\-\d{1,2}\-\d{1,2}$/.test(dateString);
    // Parse the date parts to integers
    var parts = dateString.split("-");
    var day = parseInt(parts[2], 10);
    var month = parseInt(parts[1], 10);
    var year = parseInt(parts[0], 10);

    if (isValid){
      // Check the range of month 
      isValid = !( month == 0 || month > 12);
      if (isValid){
        var monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

        // Adjust for leap years
        if(year % 400 == 0 || (year % 100 != 0 && year % 4 == 0))
            monthLength[1] = 29;

        // Check the range of the day
        isValid =  day > 0 && day <= monthLength[month - 1];
      }
    }
    if (!isValid) {
      form.input_date.style.backgroundColor = '#fba';
      document.getElementById('messg').innerHTML = "Date must be in YYYY-MM-DD format";
      document.getElementById('messg').style.display = 'inline-flex';
      return false;
    }
    else{
      document.getElementById('messg').style.display = 'none';
      form.input_date.style.backgroundColor = '#FFF';
      return true;
    }
};

function isValidHour(form, name)
{
  var hourString = '';
  if (name=="input_begin"){
    hourString = form.input_begin.value;
  }
  else if (name=='input_end'){
    hourString = form.input_end.value;
  }
  if (hourString != ''){
    // First check for the pattern
    var isValid = /^\d{1,2}\:\d{2}$/.test(hourString);
    // Parse the hour parts to integers
    var parts = hourString.split(":");
    var hour = parseInt(parts[0], 10);
    var minutes = parseInt(parts[1], 10);

    if (isValid){
      // Check the range of hours and minutes
      isValid = !(hour >= 24 || minutes >= 60);
    }
    if (!isValid) {
      if (name == 'input_begin')
        form.input_begin.style.backgroundColor = '#fba';
      else form.input_end.style.backgroundColor = '#fba';
      document.getElementById('messg').innerHTML = "Hour must be in HH:MM format";
      document.getElementById('messg').style.display = 'inline-flex';
      return false;
    }
    else{
      document.getElementById('messg').style.display = 'none';
      if (name == 'input_begin')
        form.input_begin.style.backgroundColor = '#fff';
      else form.input_end.style.backgroundColor = '#fff';
      return true;
    }
  }
  return false;
};

function checkBookForm()
{
  form = document.getElementById('inputForm');
  var isValid = isValidDate(form);
  if (isValid){
    isValid = isValidHour(form, 'input_begin');
    if (isValid){
      isValidHour(form, 'input_end');  
      if (isValid){
        isValid = form.input_end.value > form.input_begin.value
        if (isValid){
          form.submit();
        }
        else{
          document.getElementById('messg').innerHTML = "Incorrect timespan";
          document.getElementById('messg').style.display = 'inline-flex';
        }
      }
    }
  }
};

function checkForm(form)
{
  if (form == "inputForm"){
    form = document.getElementById('inputForm');
  }
  //check email and password 
  var emailString = form.email.value;
  var isValid = (emailString == '') || /\S+@\S+\.\S+/.test(emailString);
  if (!isValid){
    form.email.style.backgroundColor = '#fba';
    document.getElementById('messg').innerHTML = "Enter valid email address";
    document.getElementById('messg').style.display = 'inline-flex';
    return false;
  }
  else{

    var psswrdStr = form.password.value;
    var repsswrdStr = form.repassword.value;
    if (psswrdStr == ''){
      form.password.value = '';
      form.repassword.value = '';
      document.getElementById('messg').innerHTML = "Password cannot be empty";
      document.getElementById('messg').style.display = 'inline-flex';
      return false;
    }
    isValid = psswrdStr == repsswrdStr;
    if (!isValid){
      form.password.value = '';
      form.repassword.value = '';
      document.getElementById('messg').innerHTML = "Passwords do not match";
      document.getElementById('messg').style.display = 'inline-flex';
      return false;
    }
    else{
      document.getElementById('messg').style.display = 'none';
      form.email.style.backgroundColor = '#fff';
      console.log('submit');
      form.submit();
      
    }
  }
};