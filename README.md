# mkpipe-loader-oracledb

Oracle Database loader plugin for [MkPipe](https://github.com/mkpipe-etl/mkpipe). Writes Spark DataFrames into Oracle tables via JDBC.

## Documentation

For more detailed documentation, please visit the [GitHub repository](https://github.com/mkpipe-etl/mkpipe).

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---

## Connection Configuration

```yaml
connections:
  oracle_target:
    variant: oracledb
    host: localhost
    port: 1521
    database: ORCL
    user: myuser
    password: mypassword
```

---

## Table Configuration

```yaml
pipelines:
  - name: pg_to_oracle
    source: pg_source
    destination: oracle_target
    tables:
      - name: public.events
        target_name: MYSCHEMA.STG_EVENTS
        replication_method: full
        batchsize: 10000
```

---

## Write Parallelism & Throughput

```yaml
      - name: public.events
        target_name: MYSCHEMA.STG_EVENTS
        replication_method: full
        batchsize: 10000
        write_partitions: 4
```

- **`batchsize`**: rows per JDBC batch insert. Oracle handles large batches (10,000–50,000) well.
- **`write_partitions`**: reduces concurrent JDBC connections via `coalesce(N)`.

---

## All Table Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `name` | string | required | Source table name |
| `target_name` | string | required | Oracle destination table name (include schema) |
| `replication_method` | `full` / `incremental` | `full` | Replication strategy |
| `batchsize` | int | `10000` | Rows per JDBC batch insert |
| `write_partitions` | int | — | Coalesce DataFrame to N partitions before writing |
| `dedup_columns` | list | — | Columns used for `mkpipe_id` hash deduplication |
| `tags` | list | `[]` | Tags for selective pipeline execution |
| `pass_on_error` | bool | `false` | Skip table on error instead of failing |
