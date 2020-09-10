import subprocess


class Beaker(object):
    """"""
    CMDs = dict(
        # this cmd will make sure the given host boot from local disk
        clear_netboot=("bkr system-power "
                       "--action none "
                       "--clear-netboot {bkr_name}"),
        power_on=("bkr system-power "
                  "--action on {bkr_name}"),
        power_off=("bkr system-power "
                   "--action off {bkr_name}"),
        reboot=("bkr system-power "
                "--action reboot {bkr_name}"),
        reserve="bkr system-reserve {bkr_name}",
        release="bkr system-release {bkr_name}",
        status="bkr system-status {bkr_name} --format json")

    def _exec_cmd(self, cmd, args, output=False):
        _cmd = self.CMDs[cmd].format(**args)
        if not output:
            ret = subprocess.call(_cmd, shell=True)
            return ret
        else:
            ret = subprocess.check_output(_cmd, shell=True)
            return ret

    def power_on(self, bkr_name):
        """pass"""
        return self._exec_cmd('power_on', dict(bkr_name=bkr_name))

    def power_off(self, bkr_name):
        """pass"""
        return self._exec_cmd('power_off', dict(bkr_name=bkr_name))

    def reboot(self, bkr_name):
        """pass"""
        return self._exec_cmd('reboot', dict(bkr_name=bkr_name))

    def reserve(self, bkr_name):
        """pass"""
        return self._exec_cmd('reserve', dict(bkr_name=bkr_name))

    def release(self, bkr_name):
        """pass"""
        return self._exec_cmd('release', dict(bkr_name=bkr_name))


def check_beaker_client_ready():
    """"""
    # TODO
    pass
