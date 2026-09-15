(function (global, doc) {
    const errorPageContainer = doc.querySelector('.page-not-found');
    const specialVersions = ['latest', 'saas'];
    const latestVersionNumber = '5.0';

    if (!errorPageContainer) {
        return;
    }

    // Find the correct version
    let branchName = latestVersionNumber;
    const branchNameRegexp = /\/en\/([a-z0-9-_.]*)\//g.exec(document.location.href);

    if (branchNameRegexp !== null && branchNameRegexp.hasOwnProperty(1) && branchNameRegexp[1].length) {
        branchName = branchNameRegexp[1];
    }

    if (!/^\d+\.\d+$/.test(branchName) && !specialVersions.includes(branchName)) {
        branchName = latestVersionNumber;
    }


    // Replace all links in the TOC and in the error page content
    doc.querySelectorAll('.md-sidebar--primary .md-nav__item a, .page-not-found a').forEach(link => {
        link.href = link.href.replace(/\/en\/([a-z0-9-_.]*)\//, `/en/${branchName}/`);
    });

    // Use the 404 URL path in initial search query
    const searchLink = document.querySelector('#search-link');
    const suffix = window.location.href.split('/en/' + branchName + '/')[1];

    const searchQuery = suffix.replaceAll('/', ' ').replaceAll('_', ' ');
    searchLink.href = searchLink.href.replace('?sq=', '?sq=' + encodeURIComponent(searchQuery));

})(window, window.document);
