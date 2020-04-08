$(document).ready(function() {
	$('#like_submit').click(function() {
		var name_slug;
		var user;
		name_slug = $(this).attr('name');
		user = $(this).attr('user');
		
		$.get('/pawbook/like_post/',
			{'name_slug': name_slug,
			'user': user},
			function(data) {
				$('#like_count').html(data);
			})
	});
});

$(document).ready(function() {
	$('#dislike_submit').click(function() {
		var name_slug;
		var user;
		name_slug = $(this).attr('name');
		user = $(this).attr('user');
		
		$.get('/pawbook/dislike_post/',
			{'name_slug': name_slug,
			'user': user},
			function(data) {
				$('#dislike_count').html(data);
			})
	});
});
