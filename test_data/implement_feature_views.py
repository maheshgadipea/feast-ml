import csv
from feast import FileSource, Entity, FeatureView, Field
from feast.types import Float32, Int64

# Define the data source
driver_activity_source = FileSource(
    file_path="my_data.csv",
    csv_options={"delimiter": ","}
)

# Define the entities
driver = Entity(name="driver", join_keys=["driver_id"])

trips_today_feature = Field(name="trips_today", dtype=Int64)
rating_feature = Field(name="rating", dtype=Float32)

# Define the feature view
driver_activity_fv = FeatureView(
    name="driver_activity",
    entities=[driver],
    schema=[trips_today_feature, rating_feature],
    source=driver_activity_source,
)

# Register the feature view with Feast
feast.FeatureView.create(driver_activity_fv)
