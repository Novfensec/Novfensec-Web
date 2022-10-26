let script = document.createElement('script');
script.type = 'text/javascript';
script.referrerPolicy = "origin";
script.src = 'https://cdn.tiny.cloud/1/3bi5tqxs96aosi40ui0aldvhs945ax8b33j261xj01rxq33c/tinymce/6/tinymce.min.js';
document.head.appendChild(script);

script.onload = function () {
    tinymce.init({
        selector: '#id_content',
        plugins: [
            'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak', 'autolink', 'lists', 'table', 'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime', 'media', 'nonbreaking',
            'codesample',
            'table', 'emoticons', 'template', 'help'
        ],
        codesample_languages: [
            { text: 'HTML/XML', value: 'markup' },
            { text: 'JavaScript', value: 'javascript' },
            { text: 'CSS', value: 'css' },
            { text: 'PHP', value: 'php' },
            { text: 'Ruby', value: 'ruby' },
            { text: 'Python', value: 'python' },
            { text: 'Java', value: 'java' },
            { text: 'C', value: 'c' },
            { text: 'C#', value: 'csharp' },
            { text: 'C++', value: 'cpp' }
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | code |' +
            'bullist numlist outdent indent | codesample | image editimage | print preview media fullpage | ' +
            'a11ycheck addcomment showcomments casechange checklist export formatpainter editimage pageembed permanentpen table tableofcontents' +
            'forecolor backcolor emoticons | help',
        menu: {
            favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        codesample_global_css: true,
        toolbar_mode: 'floating',
        tinycomments_mode: 'embedded',
        tinycomments_author: 'Novfensec'
    });
}