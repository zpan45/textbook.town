//Mustache Rendering System.
function render(target, template, data, mode){
	$.get(template, function(tmp) {
		var rendered = Mustache.render(tmp, data);

		//Append vs override mode
		if(mode == "APPEND_MODE"){
			$(target).append(rendered);
		}
		else{
			$(target).html(rendered);
		}
	});
}

















//Based on:
//Render Menu from menu template
	//Mustache Templates: https://github.com/janl/mustache.js/
	/*$.get('tp/menu.html', function(template) {
		var rendered = Mustache.render(template, {
			auth_action: "#",
			auth_link: "Login"
		});
		$('#menu').html(rendered);
	});*/
//For future use in login system: http://stackoverflow.com/questions/7100294/json-post-with-customized-httpheader-field