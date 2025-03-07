document.addEventListener('DOMContentLoaded', function() {
    const articleImages = document.querySelectorAll('article img');
    
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
