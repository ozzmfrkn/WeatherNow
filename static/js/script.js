document.addEventListener('DOMContentLoaded', function() {
    const body = document.body;
    const durum = '{{ veri.durum | default("") }}'.toLowerCase();
    body.style.background = '';
    if (durum.includes('açık')) {
        body.style.background = 'linear-gradient(to right, #e67e22, #f1c40f)';
    } else if (durum.includes('yağmur') || durum.includes('yagmur')) {
        body.style.background = 'linear-gradient(to right, #34495e, #2c3e50)';
    } else if (durum.includes('bulut')) {
        body.style.background = 'linear-gradient(to right, #7f8c8d, #95a5a6)';
    } else {
        body.style.background = 'linear-gradient(to right, #2c3e50, #4b5e7a)';
    }
    const tabs = document.querySelectorAll('#weatherTabs .nav-link');
    tabs.forEach(tab => {
        tab.addEventListener('shown.bs.tab', function () {
            const panes = document.querySelectorAll('.tab-pane');
            panes.forEach(pane => {
                pane.classList.add('animate__animated', 'animate__fadeIn');
                setTimeout(() => {
                    pane.classList.remove('animate__animated', 'animate__fadeIn');
                }, 500);
            });
        });
    });
});