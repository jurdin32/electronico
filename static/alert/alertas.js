function notificacion(tiempo,tipo, mensaje,href) {
    let timerInterval
    Swal.fire({
        title: 'Todo va bien',
        html: 'Generando, ya falta poco <b></b> Milisegundos.',
        timer: tiempo,
        timerProgressBar: true,
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading()
            const b = Swal.getHtmlContainer().querySelector('b')
            timerInterval = setInterval(() => {
                b.textContent = Swal.getTimerLeft()
            }, 100)
        },
        willClose: () => {
            clearInterval(timerInterval)
            Swal.fire({
                position: 'top-end',
                icon: tipo,
                title: mensaje,
                showConfirmButton: false,
                timer: 1500
            })
            if (href!="") {
                setTimeout(function () {
                    window.location.href = href
                }, 2000)
            }

        }
    }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
            console.log('I was closed by the timer')
        }
    })
}