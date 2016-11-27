// bleasebemykennedy.com dynamic functionality 

/* 
Fading Navbar:
	Credit: http://stackoverflow.com/questions/17713389/how-to-hide-show-nav-bar-when-user-scrolls-up-down
*/

$(document).ready(function() {
	var width = $(window).width();
	if (width > 785) {
		$(window).scroll(function() {
			var scrollTop = $(this).scrollTop();
			if (scrollTop > 0) {
				$('#nav').fadeOut();
				$('#home-nav').fadeOut();
			} else {
				$('#nav').fadeIn();
				$('#home-nav').fadeIn();
			}
		});
	}; 
});


/* 
 Navigation dropdown mobile device menu:
 	Credit: https://codepen.io/RRoberts/pen/OXxkzm
*/

$(document).ready(function() {
	$(".mobile-two .menu-toggle").click(function() {
		$(this).parent().next(".mobile-nav").toggle(0 , "display");
	});
});


/*
 RSVP Form Add Guest Functionality
*/

$(document).ready(function() {
	
	// declare primary variables
	var ags = [$("span#guest_1"), $("span#guest_2"), $("span#guest_3")]
	var agButton = $("button#add_guest_button.button-primary")
	var limit = $("span#guest_limit")
	var agCounter = 0
	var guestField = $("select#guests.u-half-width")

	// initial state
	ags.forEach(function(x){x.hide();});
	limit.hide();
	agButton.hide();

	// hide/show "Add Guest" Button
	guestField.change(function() {
		if ($(this).val() == 'Yes') {
			agButton.show();
		} else {
			ags = [$("span#guest_1"), $("span#guest_2"), $("span#guest_3")];
			agCounter = 0;
			ags.forEach(function(x){x.hide();});
			agButton.hide();
			limit.hide();
		}
	});

	// add "Guest" field 
	agButton.click(function() {
		if (agCounter == 3) {
			limit.show();
		} else {
			var element = ags.shift();
			element.show();
			agCounter += 1;
		}
	});
});


/* 
 Resize RSVP Form Fields based on device
*/

$(document).ready(function(){
	var form_name = $('#name')
	var form_email = $('#email')
	var form_events = $('#events')
	var form_guests = $('#guests')
	var width = $(window).width();
	if (width < 400){
		form_name.css('width', '100%');
		form_email.css('width', '100%');
		form_events.css('width', '100%');
		form_guests.css('width', '100%');
	};
});









