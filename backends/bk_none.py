# Manage data under mlmmj spool directory directly.
import os

from libs import utils
import settings


def is_domain_exists(domain, *args, **kw):
    return True


def is_email_exists(mail, *args, **kw):
    return False


def is_maillist_exists(mail, *args, **kw):
    return True


def add_maillist(mail, *args, **kw):
    return (True, )


def update_maillist(mail, *args, **kw):
    return (True, )


def remove_maillist(mail, *args, **kw):
    return (True, )


def get_existing_maillists(domains=None, *args, **kw):
    """Get existing mailing lists.

    :param domains: a list/tuple/set of valid domain names.
                    Used if you want to get mailing lists under given domains.
    """
    if domains:
        domains = [str(d).lower() for d in domains if utils.is_domain(d)]

    # Get all directories which store mailing list accounts.
    parent_dirs = []

    if domains:
        for d in domains:
            _dir = os.path.join(settings.MLMMJ_SPOOL_DIR, d)
            parent_dirs.append(_dir)
    else:
        try:
            fns = os.listdir(settings.MLMMJ_SPOOL_DIR)
        except Exception, e:
            return (False, repr(e))

        for fn in fns:
            _dir = os.path.join(settings.MLMMJ_SPOOL_DIR, fn)
            parent_dirs.append(_dir)

    # Get all mailing lists.
    all_lists = []

    # List all directories
    for d in parent_dirs:
        try:
            fns = os.listdir(d)

            # Construct email address
            for fn in fns:
                mail = fn + '@' + os.path.basename(d)
                all_lists.append(mail)
        except Exception, e:
            return (False, repr(e))

    all_lists.sort()

    return (True, all_lists)
