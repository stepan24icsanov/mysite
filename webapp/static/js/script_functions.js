function dateTrans(dt, element) {
    let date = moment.utc(dt);
    let el_with_date = document.getElementById(element);
    let post_date_to_local_time = moment(date.local().format(), 'YYYY-MM-DD');
    let current_date = moment(moment().local().format(),'YYYY-MM-DD');
    let timedelta = +current_date.diff(post_date_to_local_time, 'days');
    if (timedelta == 0) {
        el_with_date.innerHTML = date.local().format('Сегодня в HH:mm');
    }
    else {
        if (timedelta == 1) {
            el_with_date.innerHTML = date.local().format('Вчера в HH:mm');
        }
        else{
            el_with_date.innerHTML = date.local().format('HH:mm | DD MMM YYYY');
        }
    }
}
