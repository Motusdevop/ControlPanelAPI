function sendJSON(button) {
	// с помощью jQuery обращаемся к элементам на странице по их имена
	if ((button.style.background == 'red') | (button.style.background == '')) {
		button.style.background = 'green'
        on = true
	} else {
		button.style.background = 'red'
        on = false
	}
	// а вот сюда мы поместим ответ от сервера
	let data = {
    id: button.id,
    on: on
    };

    let response = fetch('/change', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
    });

    let result = response.json;
};

async function load_buttons() {
    button1 = document.querySelector('#one');
    button2 = document.querySelector('#two');

    let url = '/state'
    let response = await fetch(url)

    let data = await response.json() // читаем ответ в формате JSON

    if (data.one){
        button1.style.background = 'green';
    };
    if (data.two){
        button2.style.background = 'green';
    };
};