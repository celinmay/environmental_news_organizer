var full-group = $("svg.eu-map > *");

full-group.on("click", function(){
	full-group.removeClass("selected");
	$(this).toggleClass("active");
});

