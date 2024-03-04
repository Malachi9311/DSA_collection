#!/usr/bin/node

TowersOfHanoi = (disks, begin=1, end=3) => {
    if (disks) {
        TowersOfHanoi(disks - 1, begin, 6 - begin - end);
        console.log("disk " + disks + " moved from " + begin + " to " + end);
        TowersOfHanoi(disks - 1, 6 - begin - end, end);
    }
}

TowersOfHanoi(3)