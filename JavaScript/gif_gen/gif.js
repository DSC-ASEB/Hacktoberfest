//api key: YOUR_API_KEY

let button_gif = document.querySelector("#get_gif")

/*when button is clicked then 
send_api_request() ->is called*/
button_gif.addEventListener("click",()=>{
	send_api_request()
})

//fetch data from gify api

//fetch() -> will fetch the respective url that we put into it
const send_api_request = async ()=>{

	let user_input = document.querySelector('#input').value
	let response = await fetch(`https://api.giphy.com/v1/gifs/search?api_key=YOUR_API_KEY&q=${user_input}`)
	console.log(response)

	//we want json data from response
	let gif = await response.json()
	console.log(gif)
	//pass the gifs into function so that it can display it to user
	use_api_data(gif)
}

//we have to display the respective gifs that user requests
const use_api_data = (gifs)=>{
	let index = Math.floor(Math.random()*gifs.data.length)
document.querySelector("#wrapper").innerHTML = `<img src ='${gifs.data[index].images.original.url}' >`
	

}
