from mkpipe.spark import JdbcLoader


class OracledbLoader(JdbcLoader, variant='oracledb'):
    driver_name = 'oracle:thin'
    driver_jdbc = 'oracle.jdbc.OracleDriver'

    def build_jdbc_url(self):
        return (
            f'jdbc:{self.driver_name}:{self.username}/{self.password}'
            f'@//{self.host}:{self.port}/{self.database}'
            f'?oracle.jdbc.defaultNChar=true'
        )
