
document.addEventListener('DOMContentLoaded', function() {
    fetch('bookmarks.json' + '?nocache=' + (new Date()).getTime())
        .then(response => response.json())
        .then(data => displayBookmarks(data));



    // render the title, bookmarks and date
    function displayBookmarks(data) {
        document.getElementById('title').innerText = data.about.title;
        document.getElementById('date').innerText = data.about.created;

        const app = document.getElementById('app');
        const tooltip = document.getElementById('tooltip');

        data.groups.forEach(group => {
            const groupDiv = document.createElement('div');
            groupDiv.className = 'group';

            const groupTitle = document.createElement('div');
            groupTitle.className = 'group-title';
            groupTitle.textContent = group.name;
            groupDiv.appendChild(groupTitle);

            group.bookmarks.forEach(bookmark => {
                const bookmarkLink = document.createElement('a');
                bookmarkLink.className = 'bookmark';
                bookmarkLink.href = bookmark.url;
                bookmarkLink.textContent = bookmark.title;
                bookmarkLink.target = '_blank';
                if (bookmark.about) {
                    bookmarkLink.dataset.about = bookmark.about;
                    bookmarkLink.addEventListener('mouseover', function(event) {
                        tooltip.textContent = event.target.dataset.about;
                        const rect = event.target.getBoundingClientRect();
                        tooltip.style.left = rect.left + 'px';
                        tooltip.style.top = rect.bottom + window.scrollY + 'px';
                        tooltip.style.display = 'block';
                    });
                    bookmarkLink.addEventListener('mouseout', function() {
                        tooltip.style.display = 'none';
                    });
                }
                groupDiv.appendChild(bookmarkLink);
            });

            app.appendChild(groupDiv);
        });
    }


    // Footer
    const tooltip = document.getElementById('tooltip');
    const footerItems = document.querySelectorAll('.footer-item');

    footerItems.forEach(item => {
        item.addEventListener('mouseover', function (event) {
            tooltip.textContent = event.target.dataset.about;
            const rect = event.target.getBoundingClientRect();
            tooltip.style.left = rect.left + 'px';
            tooltip.style.top = (rect.bottom + window.scrollY - 40) + 'px';
            tooltip.style.display = 'block';
        });

        item.addEventListener('mouseout', function () {
            tooltip.style.display = 'none';
        });
    });



    


});
