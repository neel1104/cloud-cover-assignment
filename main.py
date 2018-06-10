import os
from CloudTravel import CloudTravel


def main():
    "main function to run the program"
    fin = open("input.txt", "r")
    fout = open('output.txt', 'w')

    n = int(fin.readline())
    for _ in xrange(n):
        # taking input
        latitude = map(float, fin.readline().rstrip().split())
        longitude = map(float, fin.readline().rstrip().split())
        canTravel = fin.readline().rstrip().split(",")
        origin = int(fin.readline())
        destination = int(fin.readline())

        # init our class
        ct = CloudTravel()

        # get result
        result = ct.shortestCourierTrip(
            latitude, longitude, canTravel, origin, destination)

        # save result
        if isinstance(result, float):
            fout.write('%f' % (result))
        else:
            fout.write('%d' % (result))
        fout.write('\n')

    fout.close()
    fin.close()


if __name__ == "__main__":
    main()
