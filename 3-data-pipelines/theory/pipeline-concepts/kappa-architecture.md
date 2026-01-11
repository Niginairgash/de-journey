# Kappa Architecture
Kappa Architecture is a data processing architecture that uses
a single streaming pipeline to handle both real-time and historical data.

### Core idea:
- Stream is the source of truth
- No separate batch layer
- Reprocessing = replaying the stream

### Main components:
- Event producers (apps, DB CDC, sensors)
- Streaming log (Kafka, Pulsar)
- Stream processing engine (Flink, Spark Streaming, Kafka Streams)
- Sink (Data Lake, DWH, OLAP, Feature Store)

### Key characteristics:
- One codebase for real-time and historical processing
- Simplified architecture compared to Lambda
- Scales well with event-driven systems
- Supports replay and reprocessing from offsets

### When to use:
- Event-driven systems
- Near real-time analytics
- Streaming-first architecture

### When NOT to use:
- Heavy batch-only workloads
- No streaming infrastructure

