const imgsContainer = document.querySelector('.containerImages');
const pageContainer = document.querySelector('.wrapper');

function imgZoommer (src) {
	if (window.innerWidth < 768) {
		return;
	}

	const imageTag = document.createElement('img');
	imageTag.src = src;

	pageContainer.className += ' dark';
	document.body.append(imageTag);

	imageTag.className += 'zoom';
	pageContainer.style.pointerEvents = 'none';
}

imgsContainer.addEventListener('click', function (event) {
	const src = event.target.src;

	if (src !== undefined) {
		imgZoommer(src);
	}
});

function deleteImgZoom () {
	const closeImg = document.querySelector('.close');

	if (closeImg == null) {
		const img = document.querySelector('.zoom');

		try {
			img.className += ' close';
		} catch (e) {
			if (e instanceof TypeError) {
				// stub
			}
		}
	} else if (closeImg instanceof Object) { // is close_img is instance of Object
		closeImg.parentNode.removeChild(closeImg);
		pageContainer.style.pointerEvents = 'auto';
		pageContainer.classList.remove('dark');
	}
}
