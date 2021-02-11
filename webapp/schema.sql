
create table sketch (
    id serial primary key,
    mode text,
    title text,
    code text,
    created timestamp without time zone default (current_timestamp at time zone 'utc'),
    last_updated timestamp without time zone default (current_timestamp at time zone 'utc')
);

create index sketch_mode_idx on sketch(mode);
create index sketch_created_idx on sketch(created);
create index sketch_last_updated_idx on sketch(last_updated);