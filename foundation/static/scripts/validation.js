function processResponse(response) {
  if(response == null)
    return;

  response = JSON.parse(response.replace(/&quot;/g,'"'));
  var originalText = "There are a lot of applications like Trello, Asana, JIRA and many more for project management. However all of them are internal. Whip! disrupts the management with also letting consumers collaborate and assign tasks for the firm. Tracking your customers' feedback has never been easier.";
  var code = response['code'];
  var message = response['message'];
  var classToAdd = "error";

  if(code == 0)
    classToAdd = "success";

  $('#info_area_text').addClass(classToAdd);
  $('#info_area_text').text(message);
  setTimeout(function() {
    $('#info_area_text').removeClass(classToAdd);
    $('#info_area_text').text(originalText);
  }, 3e3);
}
