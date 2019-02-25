import sub

from plugins.sharing_filters import (
    filter_sharing,
)


sub.jobs.append(filter_sharing)


if __name__ == '__main__':
    sub.start()
