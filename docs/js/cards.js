$(function() {
    let version_path_index = 4;
    $('.card-wrapper > div > a').each(function() {
        let destUrl = $(this).attr('href');
        if ('//' === destUrl.substring(0, 2)) {
            destUrl = document.location.protocol + destUrl;
        } else if ('/' === destUrl.substring(0, 1)) {
            destUrl = document.location.protocol + '//' + document.location.host + destUrl;
        }
        destUrl = new URL(destUrl);
        let destPath = destUrl.pathname.split('/'),
            srcPath = document.location.pathname.split('/');
        if (destPath[version_path_index] !== srcPath[version_path_index]) {
            destPath[version_path_index] = srcPath[version_path_index];
        }
        destUrl.pathname = destPath.join('/');
        $(this).attr('href', destUrl.href);
    });
});
