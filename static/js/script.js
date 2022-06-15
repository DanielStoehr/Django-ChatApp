async function sendMessage(user) {
  let token = getCookie("csrftoken");
  let form = new FormData();
  form.append("textmessage", messageField.value);
  form.append("csrfmiddlewaretoken", token);
  try {
    messageContainer.innerHTML += `<p id='deleteMessage'>
                  <span class="color-gray">[${getDateString()}]</span> ${user}: <i class="color-gray">${
      messageField.value
    }</i>
              </p>`;
    const response = await fetch("/chat/", { method: "POST", body: form });
    const json = await response.json();
    const data = JSON.parse(json);
    debugger;
    document.getElementById("deleteMessage").remove();
    messageContainer.innerHTML += `<p>
                  <span class="color-gray">[${data[0].fields.created_at}]</span> ${data[1].fields.username}: <i>${data[0].fields.text}</i>
              </p>`;
    messageField.value = "";
  } catch (e) {
    console.log("An error occured", e);
  }
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function getDateString() {
  const currentDate = new Date();
  const year = currentDate.getFullYear();
  let month = currentDate.getMonth().toString();
  if (month.length == 1) {
    month = "0" + month;
  }
  let day = currentDate.getDate().toString();
  if (day.length == 1) {
    day = "0" + day;
  }
  return `${year}-${month}-${day}`;
}
