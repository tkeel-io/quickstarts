package main

import (
	"encoding/json"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

func jsonToMap(s string) map[string]any {
	resp := make(map[string]interface{})
	if err := json.Unmarshal([]byte(s), &resp); err != nil {
		log.Println(err)
	}
	return resp
}

func handlerIdentity(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H(jsonToMap(`{
    "res": {"ret": 0, "msg": "ok"},
    "plugin_id": "tkeel-device-template",
    "version": "v0.0.1",
    "tkeel_version": "v0.4.0",
    "implemented_plugin":
    [
        {
            "plugin":
            {
                "id": "tkeel-device",
                "version": "v0.4.1"
            },
            "addons":
            [
                {
                    "addons_point": "device-schema-change",
                    "implemented_endpoint": "ping"
                }
            ]
        }
    ]
	}`)))
}

func handlerStatus(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H(jsonToMap(`{"res": {"ret": 0, "msg": "ok"}, "status": 3}`)))
}

func handlerEnable(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H(jsonToMap(`{"res": {"ret": 0, "msg": "ok"}}`)))
}

func handlerDisable(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H(jsonToMap(`{"res": {"ret": 0, "msg": "ok"}}`)))
}

func addonsPing(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H(jsonToMap(`{"code": "io.tkeel.SUCCESS", "msg": "pong", "data": {}}`)))
}

func main() {
	r := gin.Default()
	r.GET("/v1/identify", handlerIdentity)
	r.GET("/v1/status", handlerStatus)
	r.POST("/v1/tenant/enable", handlerEnable)
	r.POST("/v1/tenant/disable", handlerDisable)
	r.POST("/ping", addonsPing)
	// listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
	if err := r.Run(); err != nil {
		log.Fatal(err)
	}
}
