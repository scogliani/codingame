#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define SIZE_DATE 11

/**
 ** The Art Of Computer Programming: Volume 4A: Combinatorial Algorithms Part 1
 ** 7.1.3: Bitwise Tricks and Techniques, section 'Packing and unpacking'
 */
struct Date
{
    int day;
    int month;
    int year;
};

struct Date get_date_format(char *str)
{
    struct Date date;
    struct tm tm;

    memset(&tm, 0, sizeof(tm));
    strptime(str, "%d.%m.%Y", &tm);
    date.day = tm.tm_mday;
    date.month = tm.tm_mon + 1;
    date.year = tm.tm_year + 1900;
    return (date);
}

_Bool eq_date(struct Date *d1, struct Date *d2)
{
    return (d1->day == d2->day
        && d1->month == d2->month
        && d1->year == d2->year);
}

_Bool is_leap_year(int year)
{
    _Bool is_leap_year;

    if (year%400 == 0)
    {
        is_leap_year = 1;
    }
    else if (year%100 == 0)
    {
        is_leap_year = 0;
    }
    else if (year%4 == 0)
    {
        is_leap_year = 1;
    }
    else
    {
        is_leap_year = 0;
    }
    return (is_leap_year);
}

int get_month_limit(int month, int year)
{
    int month_limit;

    if (month == 2)
    {
        month_limit = 28;
        if (is_leap_year(year))
        {
            month_limit = 29;
        }
    }
    else if (month == 4
            || month == 6
            || month == 9
            || month == 11)
    {
        month_limit = 30;
    }
    else
    {
        month_limit = 31;
    }
    month_limit++;
    return (month_limit);
}

void increment_date_per_one_day(struct Date *ref, struct Date *ctr)
{
    int month_limit;

    month_limit = get_month_limit(ref->month, ref->year);
    if (ctr)
    {
      ctr->day++;
    }
    ref->day++;
    if (ref->day%month_limit == 0)
    {
        ref->day = 1;
        ref->month++;
        if (ctr)
        {
          ctr->month = (ctr->month+1)%12;
          if (ctr->month == 0)
          {
            ctr->year++;
          }
        }
    }
    if (ref->month%13 == 0)
    {
        ref->month = 1;
        ref->year++;
    }
}


struct Date get_delta_date(char *begin, char *end)
{
    struct Date date_begin;
    struct Date date_end;
    struct Date ctr;
    struct Date ref;

    date_begin = get_date_format(begin);
    date_end = get_date_format(end);
    ctr.day = 0;
    ctr.month = 0;
    ctr.year = 0;
    ref.day = 1;
    ref.month = date_begin.month;
    ref.year = date_begin.year;
    while (!eq_date(&date_begin, &date_end))
    {
        increment_date_per_one_day(&date_begin, NULL);
        increment_date_per_one_day(&ref, &ctr);
    }
    return (ctr);
}

void print_delta_date(struct Date const * delta)
{
    if (delta->year > 0)
    {
        printf("%i year%s, ", delta->year, (delta->year > 1) ? ("s") : (""));
    }
    if (delta->month > 0)
    {
        printf("%i month%s, ", delta->month, (delta->month > 1) ? ("s") : (""));
    }
    printf("total %i days\n", delta->day);
}

int main(int argc, char **argv)
{
    char begin[SIZE_DATE];
    char end[SIZE_DATE];
    struct Date delta;

    scanf("%s", begin);
    scanf("%s", end);
    delta = get_delta_date(begin, end);
    print_delta_date(&delta);
    return (0);
}
