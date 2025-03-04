import httpx


class SofascoreClient:
    BASE_ENDPOINT = "https://api.sofascore.com/api/v1"

    def __init__(self):
        self.__cache = {}  # TODO: Implementar cache

    def get_events_url(self, date: str) -> str:
        return f"{self.BASE_ENDPOINT}/sport/football/scheduled-events/{date}"

    def get_events(self, date: str) -> dict:
        url = self.get_events_url(date)
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                return response.json()["events"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return []
            raise exc

    def get_event(self, event_id: int) -> dict:
        url = f"{self.BASE_ENDPOINT}/event/{event_id}"
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                return response.json()["event"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return {}
            raise exc

    def get_stats(self, event_id: int) -> dict:
        url = f"{self.BASE_ENDPOINT}/event/{event_id}/statistics"
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                return response.json()["statistics"][0]["groups"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return {}
            raise exc

    def get_incidents(self, event_id: int) -> dict:
        url = f"{self.BASE_ENDPOINT}/event/{event_id}/incidents"
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                return response.json()["incidents"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return {}
            raise exc

    def get_win_probability(self, event_id: int) -> dict:
        url = f"{self.BASE_ENDPOINT}/event/{event_id}/win-probability"
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                return response.json()["winProbability"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return {}
            raise exc
            
    def get_team(self, team_id: int) -> dict:
        url = f"{self.BASE_ENDPOINT}/team/{team_id}"
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()
                import json

                print(json.dumps(response.json()["team"], indent=4))
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return {}
            raise exc
