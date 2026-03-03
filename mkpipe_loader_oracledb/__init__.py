from mkpipe.spark import JdbcLoader

JAR_PACKAGES = ['com.oracle.database.jdbc:ojdbc11:23.6.0.24.10']


class OracledbLoader(JdbcLoader, variant='oracledb'):
    driver_name = 'oracle:thin'
    driver_jdbc = 'oracle.jdbc.OracleDriver'

    def build_jdbc_url(self):
        return (
            f'jdbc:{self.driver_name}:{self.username}/{self.password}'
            f'@//{self.host}:{self.port}/{self.database}'
            f'?oracle.jdbc.defaultNChar=true'
        )
