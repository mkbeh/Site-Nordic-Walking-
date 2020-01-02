let darkLayer = document.body.children[0];
const wrapper = document.querySelector('.wrapper');
const footer = document.querySelector('.footer');
const totalHeight = String(wrapper.offsetHeight + footer.offsetHeight + 20) + 'px';
const arrayClassesDarkLayerDiv = document.body.children[0].classList;
let arrayOfLi = document.querySelectorAll('#menu > li'); //	it's object
let arrayOfLiWithId = [];

function openMenu () {
	document.getElementById('menu').classList.toggle('active');
	document.getElementById('head__toggle-btn').classList.toggle('active');

	if (arrayClassesDarkLayerDiv.contains('darkLayer') !== true) {
		darkLayer.className += ' darkLayer';
		darkLayer.style.height = totalHeight;
	} else {
		for (let i = arrayOfLi.length - 1; i > 0; i--) {
			if (arrayOfLi[i].id !== '') {
				arrayOfLiWithId.push(arrayOfLi[i]);
			}
		}

		let arrayOfLiWithIdLength = arrayOfLiWithId.length; //	Раньше объявить нельзя

		for (let j = arrayOfLiWithIdLength - 1; j >= 0; j--) {
			if (arrayOfLiWithId[j].className === 'active') {
				arrayOfLiWithId[j].classList.remove('active');
			}
		}

		darkLayer.style.height = 0;
		darkLayer.classList.remove('darkLayer');		
	}
}

function checkWindowWidth (pageName) {
	if (window.innerWidth < 1024) {
		document.getElementById(pageName).classList.toggle('active');
	}
}

function openSubMenu (pageName) {
	checkWindowWidth(pageName);
}