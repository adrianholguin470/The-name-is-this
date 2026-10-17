const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/playbook.html', { waitUntil: 'load' });
  await p.pdf({ path: 'Kevins_Board_Playbook.pdf', format: 'Letter', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:7.5pt;color:#1c2430;opacity:.5;padding:0 0.75in;display:flex;justify-content:space-between;"><span style="white-space:nowrap">CannaShark Consulting, LLC · Beverly Hills, CA · cannasharkconsulting.com</span><span style="white-space:nowrap">Kevin\'s Board Playbook · page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>' });
  await b.close();
})();
