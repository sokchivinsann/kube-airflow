FROM apache/airflow:3.1.7-python3.10
USER root

RUN curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' | sudo gpg --dearmor -o /usr/share/keyrings/clickhouse-keyring.gpg \
&& ARCH=$(dpkg --print-architecture) \
&& echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg arch=${ARCH}] https://packages.clickhouse.com/deb stable main" | sudo tee /etc/apt/sources.list.d/clickhouse.list \
&& sudo apt-get update
RUN apt-get install -y --no-install-recommends clickhouse-client
COPY requirements.txt /requirements.txt
# RUN apt-get update && apt-get install -y curl ca-certificates && \
#     curl -LO "https://dl.k8s.io/release/v1.30.0/bin/linux/amd64/kubectl" && \
#     install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
#     rm kubectl && \
#     apt-get clean

USER airflow
RUN pip install --no-cache-dir "pyspark==3.5.1"
RUN pip install --no-cache-dir -r /requirements.txt \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.7/constraints-3.10.txt"

RUN pip install --no-cache-dir airflow-clickhouse-plugin clickhouse-connect clickhouse-driver
# dbt in its own venv, unconstrained
RUN python -m venv /home/airflow/dbt-venv && \
    /home/airflow/dbt-venv/bin/pip install --no-cache-dir \
      dbt-core dbt-clickhouse dbt-osmosis
