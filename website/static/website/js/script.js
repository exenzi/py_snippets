hljs.highlightAll();

let buttons = document.querySelectorAll('.copy-to-clipboard')
buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        e.preventDefault()
        copyToClipboard(e.target)
    })
})

async function copyToClipboard(target) {
    let popover = new bootstrap.Popover(target)
    slug = target.getAttribute('data')
    let code = document.getElementById(slug)
    if (!navigator.clipboard) {
        // Clipboard API not available
        return
    }
    try {
        await navigator.clipboard.writeText(code.innerText)
        popover.show()
        setInterval(() => { popover.hide(); }, 1000)
    } catch (err) {
        console.error('Failed to copy!', err)
    }
}