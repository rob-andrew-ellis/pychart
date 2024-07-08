from term_piechart import Pie
import argparse

def main() -> None:
    togo, done = read_hours()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'hours_passed', 
        help='A number representing how many hours have passed (supports floats)',
        type=float
    )

    args = parser.parse_args()

    togo -= args.hours_passed
    done += args.hours_passed

    write_hours(togo, done)

    print(generate_piechart(togo, done))

def generate_piechart(togo: float, done: float) -> Pie:
    requests = [
        {'name': 'Remaining', 'value': togo},
        {'name': 'Completed', 'value': done},
    ]

    return Pie(
        requests,
        radius=9,
        autocolor=True,
        autocolor_pastel_factor=1,
        fill='⬤',
        legend={'line': 0, 'format': '{label} {name:<8} {percent:>5.2f}% [{value}]'}
    )

def read_hours() -> tuple[float, float]:
    f = open('hours.txt', 'r')
    hours = f.readlines()
    f.close()
    togo = float(hours[0])
    done = float(hours[1])

    return togo, done

def write_hours(togo: float, done: float) -> None:
    f = open('hours.txt', 'w')
    f.write(str(togo) + '\n')
    f.write(str(done))
    f.close()

if __name__ == '__main__':
    main()

