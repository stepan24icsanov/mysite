$(document).ready(function() {
            $('#warning').hide();
			$('#signin').on('click', function() {
					let login = document.getElementById('InputLogin').value;
					let password = document.getElementById('InputPassword').value;
					$.ajax({
							url: '/login',
							method: 'post',
							dataType: 'html',
							data: {
								'login': login,
								'password': password
							},
							success: function(data) {
							        dt = JSON.parse(data);
									if (dt['status'] == 'ok') {
									    window.location.replace(window.location.protocol + "//" + window.location.host + "/" + window.location.pathname + window.location.search);
									}
									if (dt['status'] == 'wrong password') {
									    $('#warning').text('Неверный пароль');
									    $('#warning').show();
									}
									if (dt['status'] == 'not ok') {
									    $('#warning').text('Такого пользователя не существует');
									    $('#warning').show();
									}

							}
						});
					}
				);
			}
		);

