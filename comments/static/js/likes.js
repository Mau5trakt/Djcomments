console.log("loaded file")


function update_likes(post_id, qty){
    //Arguments: post_id, qty

    /*Imma do this hard coding it. If i do pagination this gonna need refactoring bc won't work
    Ok, the idea is this, due the most recent post is on the top of the page I know
    how many comments there are i can get the element of the HTML collection by
    total post - position and i can easily access to de div i gotta modify :)

    example
    if there are 5 comments the fist comment it's gonna be like
    comment # 5

    then i'll get an object like
    HTMLCollection {0: div.card... 4: div.card, length :5}

    if i need to access the div with the id  # 2 (position 3 in the HTMLCollection)
    HTMLColection{length - post_id} -> 5 - 2 = 3 :)
     */
    let divs = document.getElementsByClassName('card')
    //console.log(divs)
    //console.log(divs[0])
    //console.log(divs.length)
    let modify = divs[divs.length - post_id];
    modify.querySelector('#like-qty').textContent = String(qty)

}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



let send = id => {fetch('/comments/likes/', {
    method: 'POST',
    credentials: 'same-origin',
    headers:{
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
        },
    body: JSON.stringify({'id': id}) //JavaScript object of data to POST
    })
        .then(response => {
            return response.json() //Convert response to JSON
        })
        .then(data => {
            console.log(data)
            update_likes(data['post_id'], data['likes'])

            // Here i could work with the data to render in the screen

    //Perform actions with the response data from the view
    })}

//AFTER FUNCTIONS


let buttons = document.querySelectorAll('#btn')

for (let button of buttons)
{
    button.addEventListener('click', () => {
        console.log("Clicked");
        //console.log(button.parentNode)
        let parentDiv = button.parentNode;
        let arrContent = parentDiv.querySelector('h6').textContent.split(' ')
        let id = arrContent[arrContent.length - 1];
        send(id)


    })
}

