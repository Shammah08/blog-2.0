// //Nav Slider

// const burger = document.querySelector('.burger');
// const navLinks = document.querySelector('.nav-links');
// const navItem = document.querySelectorAll('.nav-links li');

// console.log(document.title)
// try {
//     burger.addEventListener('click', () => {
//         navLinks.classList.toggle('nav-active');
//         navItem.forEach((nav) => {
//             nav.style.opacity = 1;
//         })
//     });
// } catch (error) {
//     console.log(error)
// }




// try {
//     const dayContainer = document.querySelector('.day');
//     const dateContainer = document.querySelector('.date');
//     const hourContainer = document.querySelector('.hour');
//     const minuteContainer = document.querySelector('.minute');
//     const secondContainer = document.querySelector('.second');
//     const dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

//     function realTime() {

//         setInterval(() => {
//             const hour = new Date().getHours();
//             const minute = new Date().getMinutes();
//             const second = new Date().getSeconds();
//             const date = new Date().getDate();
//             const day = new Date().getDay();

//             // secondContainer.style.tranform = 'translateZ(360deg)';
//             // secondContainer.style.transition = 'all ease-in 1s';

//             dateContainer.innerHTML = date;
//             hourContainer.innerHTML = hour;
//             minuteContainer.innerHTML = minute;
//             secondContainer.innerHTML = second;
//             dayContainer.innerHTML = dayOfWeek[day];
//         }, 1000)
//     };

//     // real Time function call
//     realTime();
// } catch (error) {
//     if (error) {
//         console.log(error)
//     } else {
//         realTime();
//     }
// }

// // console.log('Hello');
// const articles = document.querySelectorAll("article.article");

// try {
//     articles.forEach(article => {
//         article.addEventListener('mouseenter', () => {
//             article.children[0].style.display = 'none';
//             article.children[1].style.display = 'flex';
//         })
//         article.addEventListener('mouseleave', () => {
//             article.children[0].style.display = 'flex';
//             article.children[1].style.display = 'none';
//         })
//     })


// } catch (error) {
//     console.log(error)
// }





// try {
//     //Followers
//     const followBtn = document.querySelector('.follow');

//     followBtn.addEventListener('click', () => {
//         const status = followBtn.textContent;
//         const followerSpan = document.createElement('span');
//         followerSpan.classList.add('follower-prompt');
//         const followSection = document.querySelector('.follow-section')
//         followSection.appendChild(followerSpan);


//         if (status == 'Follow') {
//             followBtn.textContent = 'Following';
//             followBtn.style.color = 'black';
//             followBtn.style.backgroundColor = 'white';
//             followerSpan.innerHTML = `You are now following ${document.getElementById('username').textContent} `;
//             const followers = document.querySelector('.followers');
//             //console.log(Number(followers.innerHTML) + 10);
//             followers.innerHTML = Number(followers.innerHTML) + 1;
//             setTimeout(() => {
//                 followerSpan.innerHTML = ' ';
//             }, 1500)

//         }
//         else {
//             followBtn.textContent = 'Follow';
//             followBtn.style.color = 'white';
//             followBtn.style.backgroundColor = 'red';
//             const followers = document.querySelector('.followers');
//             //console.log(Number(followers) + 10);
//             followers.innerHTML = Number(followers.innerHTML) - 1;

//             followerSpan.innerHTML = `You have unfollowed ${document.getElementById('username').textContent} `;
//             setTimeout(() => {
//                 followerSpan.innerHTML = ' ';
//             }, 1500)
//         };

//     });

// } catch (error) {
//     console.log(error)
// }

//  SHOW PASSWORD


try {
    const passwordDiv = document.querySelectorAll('div.password-div')
    const showPassword = document.querySelector('div.password-div span')

    console.log(passwordDiv)  
        // console.log(event.target.innerHTML)
        div.children[0].addEventListener('keyup', event => {
            if (event.currentTarget.value) {
                div.children[1].style.display = 'flex';
            } else {
                div.children[1].style.display = 'none';
            }
        })
        passwordDiv.forEach(div => {
            div.addEventListener('click', event => {
                // console.log(div.children[1].innerText)
                // console.log(event.currentTarget.children)
                // console.log('Div =>', div)
                // console.log('Show Password =>', showPassword)
                switch (event.currentTarget.children[1].innerText) {
                    case 'Show':
                        console.log(event.currentTarget.children[1].innerText)
                        // console.log(div.children)
                        // console.log(event.target.parentElement.parentElement.children[0].type)
                        setTimeout(() => {
                            event.currentTarget.children[0].type = 'password';
                            event.currentTarget.children[1].innerText = 'Show'
                        }, 4000)
                        event.currentTarget.children[0].type = 'text';
                        event.currentTarget.children[1].innerText = 'Hide'
                        break;
                    default:
                        console.log(event.currentTarget.children[1].innerText)

                        event.currentTarget.children[0].type = 'password';
                        event.currentTarget.children[1].innerText = 'Show'
                        break;
                }
            })

        })
    })
} catch (error) {
    console.log(error)
}

// Password Match

