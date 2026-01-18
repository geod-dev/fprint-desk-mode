pkgname=fprint-desk-mode
pkgver=1.0.0
pkgrel=1
pkgdesc="Disable fingerprint reader when an external keyboard is connected"
license=('GPLv3')
depends=('fprintd' 'python')
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
options=('!debug')
source=(
    "fprint_desk_mode"
    "fdm_post_install"
    "fdm_pre_remove"
    "get_configured_system_auth.py"
    "get_unconfigured_system_auth.py"
    "fprint-desk-mode-install.hook"
    "fprint-desk-mode-remove.hook"
)
sha256sums=('795efc129c79d0bcb1b4870a1c73ef1ad11e42483898d82e029c726be8421e94'
            '2451a268f9c34caadffd6f441b94231f8a5ceff1ab45fae6ae0ba718a2ae545a'
            'f994e72a4223604a859a1256180c8f5c80ac01136770b13f7c90f81ebabdc29a'
            'b89c34f8fe59d7e002ca8e2268b1d1cf7b7477b9a160cb620512ba452f12b2ee'
            'd49eb5356d1f55c1465dee11c66d794e1e44c41f0f23652373a89ba2078854db'
            '804d96551d77ef71cc6b552823d4c1b430b0ac7a262c2d04f68a7c028fb1cde1'
            '1ec4632387c3bc6ff8afd0da9b36a8752f6f4765573d61f5d14749ed39217784')

package() {
    install -Dm755 "$srcdir/fprint_desk_mode" "$pkgdir/usr/bin/fprint_desk_mode"
    install -Dm755 "$srcdir/fdm_post_install" "$pkgdir/usr/bin/fdm_post_install"
    install -Dm755 "$srcdir/fdm_pre_remove" "$pkgdir/usr/bin/fdm_pre_remove"

    install -Dm644 "$srcdir/get_configured_system_auth.py" "$pkgdir/usr/share/fprint-desk-mode/get_configured_system_auth.py"
    install -Dm644 "$srcdir/get_unconfigured_system_auth.py" "$pkgdir/usr/share/fprint-desk-mode/get_unconfigured_system_auth.py"

    install -Dm644 "$srcdir/fprint-desk-mode-install.hook" "$pkgdir/usr/share/libalpm/hooks/fprint-desk-mode-install.hook"
    install -Dm644 "$srcdir/fprint-desk-mode-remove.hook" "$pkgdir/usr/share/libalpm/hooks/fprint-desk-mode-remove.hook"
}

