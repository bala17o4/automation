// var count = 1 
// function myfunction(){
//     if(count<=18){

//             var element = $(document.createElement('div')).attr({"id":"text_area"+count,"class":"col-sm-4"});
//             element.after().html('<label>Website Link</label>'+'<input type="text" class="form-control"  name="link'+count+'">');
//             element.appendTo("#textbox")


//             var element = $(document.createElement('div')).attr({"id":"user"+count,"class":"col-sm-4"});
//             element.after().html('<label>Username</label>'+'<input type="text" class="form-control"  name="user'+count+'">');
//             element.appendTo("#textbox")


//             var element = $(document.createElement('div')).attr({"id":"pass"+count,"class":"col-sm-4"});
//             element.after().html('<label>password</label>'+'<input type="text" class="form-control"  name="pass'+count+'">');
//             element.appendTo("#textbox")
//             count+=1
 
//     }  
// }
const togglePassword = document.querySelector("#togglePassword");
        const password = document.querySelector("#password");

        togglePassword.addEventListener("click", function () {
            // toggle the type attribute
            const type = password.getAttribute("type") === "password" ? "text" : "password";
            password.setAttribute("type", type);
            
            // toggle the icon
            this.classList.toggle("bi-eye");
        });
