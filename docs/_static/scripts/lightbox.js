document.addEventListener('DOMContentLoaded', function() {
    const imageSelector = 'article *:not(figure) > img:not(.no-lightbox), article figure:not(.no-gallery) > img';

    const articleImages = document.querySelectorAll(imageSelector);
    
    for (let i = 0; i < articleImages.length; i++) {
        let image = articleImages[i];
        let lightbox = document.createElement('a');

        lightbox.href = image.src;
        lightbox.classList.add('lightbox');
        image.parentNode.insertBefore(lightbox, image);
        lightbox.appendChild(image);
    }

    GLightbox({
        selector: '.lightbox',
        loop: true,
    });
});
